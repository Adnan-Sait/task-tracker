-- UTF - 8
\set ON_ERROR_STOP on

BEGIN;
	
	DROP TABLE IF EXISTS public."DayOverview";
	
	DROP TABLE IF EXISTS public."DailyActivity";
	
	DROP TABLE IF EXISTS public."Task";
	
	DROP TABLE IF EXISTS public."Project";
	
	DROP TABLE IF EXISTS public."MorningSchedule";
	
	DROP TABLE IF EXISTS public."TaskType";
	
	CREATE TABLE "TaskType" (
		"taskTypeId" serial,
		"taskTypeName" character varying(255) NOT NULL,
		"description" character varying,
		CONSTRAINT "taskTypeTaskTypeId_pkey" PRIMARY KEY ("taskTypeId")
	);
	
	
	CREATE TABLE "MorningSchedule" (
		"morningScheduleId" serial,
		"morningScheduleRepresentation" character varying(20) NOT NULL UNIQUE,
		"description" text,
		"createdTimestamp" timestamp with time zone DEFAULT current_timestamp,
		"modifiedTimestamp" timestamp with time zone DEFAULT current_timestamp,
		CONSTRAINT "morningScheduleMorningScheduleId_pkey" PRIMARY KEY ("morningScheduleId")
	);

	CREATE TABLE "Project" (
		"projectId" serial,
		"projectName" character varying(255) UNIQUE,
		"startTimestamp" timestamp with time zone NOT NULL,
		"description" text,
		"createdTimestamp" timestamp with time zone DEFAULT current_timestamp,
		"modifiedTimestamp" timestamp with time zone DEFAULT current_timestamp,
		CONSTRAINT "projectProjectId_pkey" PRIMARY KEY ("projectId")
	);
	
	CREATE TABLE "Task" (
		"taskId" serial,
		"taskName" character varying(255),
		"projectId" integer NOT NULL,
		"status" character varying(20) NOT NULL,
		"startTimestamp" timestamp with time zone NOT NULL,
		"completeTimestamp" timestamp with time zone,
		"description" text,
		"createdTimestamp" timestamp with time zone DEFAULT current_timestamp,
		"modifiedTimestamp" timestamp with time zone DEFAULT current_timestamp,
		CONSTRAINT "taskTaskId_pkey" PRIMARY KEY ("taskId"),
		CONSTRAINT "taskProjectId_fkey" FOREIGN KEY ("projectId") REFERENCES public."Project"("projectId"),
		CONSTRAINT "taskTaskNameProjectId_unique" UNIQUE ("taskName", "projectId")
	);
	
	CREATE TABLE "DailyActivity" (
		"dailyActivityId" serial,
		"dateRecorded" date NOT NULL,
		"taskId" integer NOT NULL,
		"effort" double precision NOT NULL,
		"description" text,
		"createdTimestamp" timestamp with time zone DEFAULT current_timestamp,
		"modifiedTimestamp" timestamp with time zone DEFAULT current_timestamp,
		CONSTRAINT "dailyActivityDailyActivityId_pkey" PRIMARY KEY ("dailyActivityId"),
		CONSTRAINT "dailyActivityTaskId_fkey" FOREIGN KEY ("taskId") REFERENCES public."Task"("taskId")
	);
	
	CREATE TABLE "DayOverview" (
		"dayOverviewId" serial,
		"dateRecorded" date NOT NULL UNIQUE,
		"startTime" time NOT NULL,
		"leavingTime" time NOT NULL,
		"workHours" double precision NOT NULL,
		"breakHours" double precision NOT NULL,
		"lunchDuration" double precision NOT NULL,
		"prayer" boolean DEFAULT FALSE NOT NULL,
		"morningScheduleId" integer NOT NULL,
		"createdTimestamp" timestamp with time zone DEFAULT current_timestamp,
		"modifiedTimestamp" timestamp with time zone DEFAULT current_timestamp,
		CONSTRAINT "dayOverviewDayOverviewId_pkey" PRIMARY KEY ("dayOverviewId"),
		CONSTRAINT "dayOverviewMorningScheduleId_fkey" FOREIGN KEY ("morningScheduleId") REFERENCES public."MorningSchedule"("morningScheduleId")
	);
	
	DROP FUNCTION IF EXISTS "updateModifiedColumn";
	
	CREATE OR REPLACE FUNCTION "updateModifiedColumn"()   
	RETURNS TRIGGER AS $$
	BEGIN
	  NEW."modifiedTimestamp" = now(); 
	  RETURN NEW;
	END;
	$$ language 'plpgsql';
	
	DROP FUNCTION IF EXISTS "updateCompletedTimestamp";
	
	CREATE OR REPLACE FUNCTION "updateCompletedTimestamp"()   
	RETURNS TRIGGER AS $$
	BEGIN
		IF (NEW."status" = 'COMPLETE') THEN
			NEW."completeTimestamp" = now();
		ELSE
			NEW."completeTimestamp" = NULL;
		END IF;
		RETURN NEW;
	END;
	$$ language 'plpgsql';

	CREATE TRIGGER "updateModifiedTimeProject" BEFORE UPDATE ON "Project" FOR EACH ROW EXECUTE PROCEDURE "updateModifiedColumn"();
	CREATE TRIGGER "updateModifiedTimeTask" BEFORE UPDATE ON "Task" FOR EACH ROW EXECUTE PROCEDURE "updateModifiedColumn"();
	CREATE TRIGGER "updateCompletedTimeTask" BEFORE UPDATE ON "Task" FOR EACH ROW EXECUTE PROCEDURE "updateCompletedTimestamp"();
	CREATE TRIGGER "updateModifiedTimeDailyActivity" BEFORE UPDATE ON "DailyActivity" FOR EACH ROW EXECUTE PROCEDURE "updateModifiedColumn"();
	CREATE TRIGGER "updateModifiedTimeMorningSchedule" BEFORE UPDATE ON "MorningSchedule" FOR EACH ROW EXECUTE PROCEDURE "updateModifiedColumn"();
	CREATE TRIGGER "updateModifiedTimeDayOverview" BEFORE UPDATE ON "DayOverview" FOR EACH ROW EXECUTE PROCEDURE "updateModifiedColumn"();
	
COMMIT;
