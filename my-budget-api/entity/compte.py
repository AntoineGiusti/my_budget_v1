from database.database_init import db


class MonCompte(db.Model):
    __tablename__ = 'mon_compte'
    id = db.Column(db.Integer, primary_key=True)
    revenu = db.Column(db.Float, unique=False, nullable=False)
    depenses_fixes = db.Column(db.Float, unique=False, nullable=False)
    imprevue = db.Column(db.Float, unique=False, nullable=False)
    reste = db.Column(db.Float, unique=False, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'revenu': self.revenu,
            'depenses_fixes': self.depenses_fixes,
            'imprevue': self.imprevue,
            'reste': self.reste
        }
