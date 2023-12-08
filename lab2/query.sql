select * from schedule s
join schedule_item i on s.schedule_item_id = i.id
join teacher t on t.id=s.teacher_id
join cabinet c on c.id=s.cabinet_id
join subject u on u.id=i.subject_id
join student_group g on g.id=s.schedule_item_id;
