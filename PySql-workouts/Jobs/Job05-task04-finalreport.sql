create or replace temp view temp_txnsdata as
select state,count(txntype) as type_count, current_date as load_dt  from inceptez_catalog.outputdb.tbltnxsvaluetype group by state;

insert into inceptez_catalog.outputdb.tblfinalreport select * from temp_txnsdata;