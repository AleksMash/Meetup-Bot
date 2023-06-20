CREATE TABLE "person" (
  "id" uuid DEFAULT gen_random_uuid(),
  "name" VARCHAR(255),
  "tg_name" VARCHAR(255),
  "tg_user_id" VARCHAR(255),
  "tg_chat_id" VARCHAR(255),
  PRIMARY KEY ("id")
);

CREATE TABLE "meetup" (
  "id" uuid DEFAULT gen_random_uuid(),
  "title" VARCHAR(255),
  "organizer" UUID,
  "description" TEXT,
  "start_date" TIMESTAMP,
  "end_date" TIMESTAMP,
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_meetup.organizer"
    FOREIGN KEY ("organizer")
      REFERENCES "person"("id")
);

CREATE TABLE "talk" (
  "id" uuid DEFAULT gen_random_uuid(),
  "title" VARCHAR(255),
  "meetup" UUID,
  "description" TEXT,
  "start_date" TIMESTAMP,
  "end_date" TIMESTAMP,
  "speaker" UUID,
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_talk.meetup"
    FOREIGN KEY ("meetup")
      REFERENCES "meetup"("id"),
  CONSTRAINT "FK_talk.speaker"
    FOREIGN KEY ("speaker")
      REFERENCES "person"("id")
);

CREATE TABLE "profile" (
  "id" uuid DEFAULT gen_random_uuid(),
  "person" UUID UNIQUE,
  "bio" TEXT,
  "website" VARCHAR(255),
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_profile.person"
    FOREIGN KEY ("person")
      REFERENCES "person"("id")
);

CREATE TABLE "question" (
  "id" uuid DEFAULT gen_random_uuid(),
  "title" VARCHAR(255),
  "talk" UUID,
  "description" TEXT,
  "author" UUID,
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_question.author"
    FOREIGN KEY ("author")
      REFERENCES "person"("id"),
  CONSTRAINT "FK_question.talk"
    FOREIGN KEY ("talk")
      REFERENCES "talk"("id")
);

CREATE TABLE "donation" (
  "id" uuid DEFAULT gen_random_uuid(),
  "donator" UUID,
  "meetup" UUID,
  "amount" MONEY,
  PRIMARY KEY ("id"),
  CONSTRAINT "FK_donation.donator"
    FOREIGN KEY ("donator")
      REFERENCES "person"("id"),
  CONSTRAINT "FK_donation.meetup"
    FOREIGN KEY ("meetup")
      REFERENCES "meetup"("id")
);
