create table std (
    id serial primary key,
    dow text,
    pyindex integer);
    
    
insert into std (dow, pyindex) values ('monday', 0);
insert into std (dow, pyindex) values ('tuesday', 1);
insert into std (dow, pyindex) values ('wednesday', 2);
insert into std (dow, pyindex) values ('thursday', 3);
insert into std (dow, pyindex) values ('friday', 4);
insert into std (dow, pyindex) values ('saturday', 5);
insert into std (dow, pyindex) values ('sunday', 6);    
