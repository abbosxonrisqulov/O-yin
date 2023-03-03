create table if not exists user(
    id serial,
    first_name varchar(64) not null,
    last_name varchar(64) not null,
    login varchar(32) not null unique,
    password varchar(32) not null
)

insert into user(first_name,last_name,login,password) 
values('Abbosxon','Risqulov','Abbos2003','q1w2e3r4');

select * 
from user
where login="{login}" 