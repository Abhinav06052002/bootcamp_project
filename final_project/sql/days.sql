create table sunday(
    id serial primary key,
    task text,
    due_time integer,
    status text,
    person serial references people(id));
    
create table monday(
    id serial primary key,
    task text,    
    due_time integer,
    status text,
    person serial references people(id));
        
create table tuesday(
    id serial primary key,
    task text,
    due_time integer,
    status text,
    person serial references people(id));    
    
create table wednesday(
    id serial primary key,
    task text,
    due_time integer,
    status text,
    person serial references people(id));
    
create table thursday(
    id serial primary key,
    task text,
    due_time integer,
    status text,
    person serial references people(id));            
    
create table friday(
    id serial primary key,
    task text,
    due_time integer,
    status text,
    person serial references people(id));    
    
create table saturday(
    id serial primary key,
    task text,
    due_time integer,
    status text,
    person serial references people(id)); 
    
    
    
    
    
       
