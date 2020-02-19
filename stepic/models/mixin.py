from stepic import db
from stepic.exceptions import SaveObjectException


# From Mike Bayer's "Building the app" talk
# https://speakerdeck.com/zzzeek/building-the-app
class BaseMixin:
    """
        A mixin that adds a surrogate integer 'primary key' column named ``id``
        to any declarative-mapped class and other usefull stuff.
    """

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the database."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            try:
                db.session.flush()
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise SaveObjectException(ex)
            else:
                return self

    def delete(self, commit=True):
        """Remove the record from the database."""
        db.session.delete(self)
        return commit and db.session.commit()

    def flush(self):
        try:
            db.session.add(self)
            db.session.flush()
        except Exception as ex:
            db.session.rollback()
            raise SaveObjectException(ex)
        else:
            return self

def reference_col(tablename, nullable=False, pk_name='id', **kwargs):
    """Column that adds primary key foreign key reference.

    Usage: ::

        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    return db.Column(
        db.ForeignKey('{0}.{1}'.format(tablename, pk_name)),
        nullable=nullable, **kwargs)
