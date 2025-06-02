
CREATE TABLE avto (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(20) NOT NULL,
    model VARCHAR(20) NOT NULL,
    narxi NUMERIC(20,2) NOT NULL
    );

CREATE TABLE userlar (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    ism VARCHAR(50) NOT NULL,
    familiya VARCHAR(50) NOT NULL,
    jinsi VARCHAR(10) NOT NULL,
    email VARCHAR(50),
    tugulgan_kun DATE NOT NULL,
    davlat VARCHAR(50) NOT NULL,
    avto_id BIGINT REFERENCES avto(id),
    UNIQUE(avto_id)
    );


INSERT INTO userlar (ism,familiya,jinsi,email,tugulgan_kun,davlat) VALUES ('Muhammadali','Sa`dulloh','Erkak','muhammadali@gmai.com','01-12-2005','Uzbekistan');
INSERT INTO userlar (ism,familiya,jinsi,email,tugulgan_kun,davlat) VALUES ('To`yboyev','Suxrob','Erkak','suxrob@gmai.com','04-06-2005','Uzbekistan');
INSERT INTO userlar (ism,familiya,jinsi,email,tugulgan_kun,davlat) VALUES ('Shukrulloyev','Behruz','Erkak','behruz@gmai.com','31-01-2005','Uzbekistan');
INSERT INTO userlar (ism,familiya,jinsi,email,tugulgan_kun,davlat) VALUES ('Bekzod','Burxonov','Erkak','bek@gmail.com','02-06-2005','Uzbekistan');
INSERT INTO userlar (ism,familiya,jinsi,email,tugulgan_kun,davlat) VALUES ('Muhammadali','Sa`dulloh','Erkak','muhammadalis@gmai.com','01-12-2005','Uzbekistan');

INSERT INTO avto (make,model,narxi) VALUES ('Chevrolet','Damas',78000000);
INSERT INTO avto (make,model,narxi) VALUES ('Lada','Jiguli 007',60000000);
INSERT INTO avto (make,model,narxi) VALUES ('Byd','Song+',350000000);
INSERT INTO avto (make,model,narxi) VALUES ('BMW','E60',200000000);