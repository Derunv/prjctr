from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData, create_engine

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{database}'
engine = create_engine(
    DATABASE_URI.format(
        host='localhost',
        database='prjctr_lessons',
        user='postgres',
        password='ee813368',
        port=5432,
    )
)
metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class StudentSubject(Base):
    __tablename__ = 'student_subject'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))

    student = relationship("Student", back_populates="student_subjects")
    subject = relationship("Subject", back_populates="subject_students")


Student.student_subjects = relationship("StudentSubject", back_populates="student")
Subject.subject_students = relationship("StudentSubject", back_populates="subject")

metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


query_result = session.query(Student.name).join(StudentSubject, StudentSubject.student_id == Student.id)\
    .join(Subject, StudentSubject.subject_id == Subject.id)\
    .filter(Subject.name == 'English').all()

# Output the result
for name in query_result:
    print(name[0])

# Close the session
session.close()

