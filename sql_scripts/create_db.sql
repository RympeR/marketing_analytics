create table work_category(
	work_category_id serial primary key,
	category_name text not null,
	category_parent_id int references work_category(work_category_id) not null
);
create table client(
	client_id serial primary key,
	login text unique not null,
	password text not null,
	work_stage float,
	salary_preference float
);

create table scrapper(
	scrapper_id serial primary key,
	address text not null,
	is_deleted boolean default false,
	is_active boolean default false,
	name text not null,
	login text,
	password  text
);

create table vacancy(
	vacancy_id serial primary key,
	vacancy_name text not null,
	expirience float,
	effectivness float,
	posted_date date,
	website_name text not null,
	salary float,
	city text,
	country text,
	company text,
	work_category_id int references work_category(work_category_id)
);

create table client_work(
	client_work_id bigserial primary key,
	client_id int references client(client_id) not null,
	work_category_id int references work_category(work_category_id) not null
);

create table client_work_preferences(
	client_work_preferences_id bigserial primary key,
	client_id int references client(client_id) not null,
	work_category_id int references work_category(work_category_id) not null
);

create table city(
	city_id serial primary key,
	city_name  text not null
);