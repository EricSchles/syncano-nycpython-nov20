drop table if exists directory;
create table directory (
       id integer primary key autoincrement,
       email text not null,
       username text not null, 
       phone integer not null,
       picture BLOB not null

);
#If any of these are empty pass in a null value rather than having to worry about this field not existing in the db.

drop table if exists account_holder;
create table account_holder(
       id integer primary key autoincrement,
       email text not null,
       password text not null,
       username text not null,
       phone integer not null,
       picture BLOB not null
);
