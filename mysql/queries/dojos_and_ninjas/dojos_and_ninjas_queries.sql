SET FOREIGN_KEY_CHECKS=0;

insert into dojos (name)
values('dallas'),('remote'),('tulsa');
	
select * from dojos;

delete from dojos where id > 0;

select * from dojos;

insert into dojos (name)
values('Konohagakure'),('Sunagakure'),('Kumogakure');

INSERT INTO `ninjas`
(`first_name`,
`last_name`,
`Dojo_id`)
VALUES
('Hashirama','Senju',1),
('Tobirama','Senju',1),
('Hiruzen','Sarutobi',1);

INSERT INTO `dojos_and_ninjas`.`ninjas`
(`first_name`,
`last_name`,
`Dojo_id`)
VALUES
('Reto','del desert',2),
('Sahmo','del desert',2),
('Gaara','del desert',2);

INSERT INTO `dojos_and_ninjas`.`ninjas`
(`first_name`,
`last_name`,
`Dojo_id`)
VALUES
('Ashina','Uzumaki',3),
('Mito','Uzumaki',3),
('Kushina','Uzumaki',3);

-- select *
-- from ninjas
-- where Dojo_id = 1;

-- select *
-- from ninjas
-- where Dojo_id = 3;

-- select Dojo_id
-- from ninjas
-- where id > id-1;




