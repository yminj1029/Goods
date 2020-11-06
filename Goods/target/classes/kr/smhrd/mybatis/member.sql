create table bigdata(
	num number not null primary key,
	name varchar2(20) not null,
	id varchar2(20) not null,
	email varchar2(40) not null,
	phone varchar2(20) not null
)

create sequence big_seq;

insert into bigdata values(big_seq.nextval, '관리자','admin','admin@naver.com','010-1111-1111');

select * from BIGDATA;