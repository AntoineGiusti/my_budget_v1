from flask_restx import Resource, fields, Namespace
from database.database_init import db
from entity.compte import MonCompte

ns = Namespace('mon_compte', description='api pour gérer le compte courant')


compte_model = ns.model('mon_compte', {
    'revenu': fields.Float,
    'depenses_fixes': fields.Float,
    'imprevue': fields.Float,
    'reste': fields.Float,
})


@ns.route('/', methods=['GET'])
class MesComptes(Resource):
    def get(self):
        return [mon_compte.to_dict() for mon_compte in MonCompte.query.order_by(MonCompte.revenu).all()]
