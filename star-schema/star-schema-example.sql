BEGIN;

CREATE TABLE "FactBilling"
(
    billid serial,
    customerid integer NOT NULL,
    monthid integer NOT NULL,
    billedamount integer NOT NULL,
    PRIMARY KEY (billid)
);

CREATE TABLE "DimMonth"
(
    monthid integer NOT NULL,
    year integer NOT NULL,
    month integer NOT NULL,
    monthname varchar(10) NOT NULL,
    quarter integer NOT NULL,
    quartername varchar(2) NOT NULL,
    PRIMARY KEY (monthid)
);

CREATE TABLE "DimCustomer"
(
    customerid integer NOT NULL,
    category varchar(10) NOT NULL,
    country varchar(40) NOT NULL,
    industry varchar(40) NOT NULL,
    PRIMARY KEY (customerid)
);

ALTER TABLE "FactBilling"
    ADD FOREIGN KEY (customerid)
    REFERENCES "DimCustomer" (customerid)
    NOT VALID;


ALTER TABLE "FactBilling"
    ADD FOREIGN KEY (monthid)
    REFERENCES public."DimMonth" (monthid)
    NOT VALID;

END;
