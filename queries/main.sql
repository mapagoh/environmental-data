CREATE TABLE `biodiversity` (
	`Country` text,
	`Mammals` decimal(8,2),
	`Birds` decimal(8,2),
	`Reptiles` decimal(8,2),
	`Amphibians` decimal(8,2),
	`Fish` decimal(8,2),
	`MarineFish` decimal(8,2),
	`FreshwaterFish` decimal(8,2),
	`VascularPlants` decimal(8,2),
	`Mosses` decimal(8,2),
	`Lichens` decimal(8,2),
	`Invertebrates` decimal(8,2)
)

BULK INSERT `biodiversity` FROM "../../data/biodiversity.csv" ;

CREATE TABLE `data` (
	`country` text,
	`1990` double,
	`1991` double,
	`1992` double,
	`1993` double,
	`1994` double,
	`1995` double,
	`1996` double,
	`1997` double,
	`1998` double,
	`1999` double,
	`2000` double,
	`2001` double,
	`2002` double,
	`2003` double,
	`2004` double,
	`2005` double,
	`2006` double,
	`2007` double,
	`2008` double,
	`2009` double,
	`2010` double,
	`2011` double,
	`2012` double,
	`2013` double,
	`2014` double,
	`2015` double,
	`2016` double,
	`2017` double,
	`2018` double,
	`2019` double,
	`2020` double
)

BULK INSERT `data` FROM "../../data/data.csv" ;

CREATE TABLE `electricity` (
	`Country` text,
	`2000` int,
	`2001` int,
	`2002` int,
	`2003` int,
	`2004` int,
	`2005` int,
	`2006` int,
	`2007` int,
	`2008` int,
	`2009` int,
	`2010` int,
	`2011` int,
	`2012` int,
	`2013` int,
	`2014` int,
	`2015` int,
	`2016` int,
	`2017` double,
	`2018` double,
	`2019` double,
	`2020` double
)

BULK INSERT `electricity` FROM "../../data/electricity.csv" ;

CREATE TABLE `water` (
	`Country` text,
	`1970` double,
	`1980` double,
	`1990` double,
	`1995` double,
	`2000` double,
	`2005` double,
	`2010` double,
	`2015` double,
	`2016` double,
	`2017` double,
	`2018` double,
	`2019` double,
	`2020` double
)

BULK INSERT `water` FROM "../../data/water.csv" ;