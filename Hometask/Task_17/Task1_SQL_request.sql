SELECT st.name FROM subject s
LEFT JOIN student_subject ss ON s.id = ss.subject_id
LEFT JOIN student st ON ss.student_id = st.id
WHERE s.name='English' ;