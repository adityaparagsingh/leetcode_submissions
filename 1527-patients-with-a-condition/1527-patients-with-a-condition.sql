select patient_id, patient_name, conditions from patients
where Conditions like "DIAB1%" OR conditions LIKE '% DIAB1%';