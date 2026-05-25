from flask import Blueprint
from controllers.user_controller import UserController
from controllers.match_controller import MatchController
from controllers.poll_controller import PollController
from controllers.album_controller import AlbumController
from controllers.ticket_controller import TicketController
from controllers.payment_gateway_controller import PaymentGatewayController

api_bp = Blueprint('api', __name__)

api_bp.add_url_rule('/register', 'register', UserController.register, methods=['POST'])
api_bp.add_url_rule('/login', 'login', UserController.login, methods=['POST'])
api_bp.add_url_rule('/profile', 'profile', UserController.get_profile, methods=['GET'])
api_bp.add_url_rule('/logout', 'logout', UserController.logout, methods=['POST'])

api_bp.add_url_rule('/matches', 'matches', MatchController.get_matches, methods=['GET'])
api_bp.add_url_rule('/matches/<int:match_id>', 'get_match', MatchController.get_match_by_id, methods=['GET'])
api_bp.add_url_rule('/matches/phase/<string:phase>', 'matches_by_phase', MatchController.get_matches_by_phase, methods=['GET'])
api_bp.add_url_rule('/matches/live', 'live_matches', MatchController.get_live_matches, methods=['GET'])
api_bp.add_url_rule('/matches/today', 'today_matches', MatchController.get_today_matches, methods=['GET'])
api_bp.add_url_rule('/matches/group/<string:group>', 'matches_by_group', MatchController.get_matches_by_group, methods=['GET'])
api_bp.add_url_rule('/standings', 'standings', MatchController.get_standings, methods=['GET'])

api_bp.add_url_rule('/polls/groups', 'create_poll_group', PollController.create_group, methods=['POST'])
api_bp.add_url_rule('/polls/groups', 'get_poll_groups', PollController.get_groups, methods=['GET'])
api_bp.add_url_rule('/polls/groups/<int:group_id>/rankings', 'get_group_rankings', PollController.get_group_rankings, methods=['GET'])

api_bp.add_url_rule('/laminas', 'get_all_laminas', AlbumController.get_all_laminas, methods=['GET'])
api_bp.add_url_rule('/album/selecciones','get_selecciones', AlbumController.get_selecciones, methods=['GET'])
api_bp.add_url_rule('/album/<seleccion>/<string:user_id>', 'get_album_seleccion', AlbumController.get_album_seleccion, methods=['GET'])
api_bp.add_url_rule('/album/especiales/<string:user_id>', 'get_especiales', AlbumController.get_especiales, methods=['GET'])
api_bp.add_url_rule('/album/progreso/<string:user_id>', 'get_progreso', AlbumController.get_progreso, methods=['GET'])
api_bp.add_url_rule('/album/open-pack/<string:user_id>', 'open_pack', AlbumController.open_pack, methods=['POST'])
api_bp.add_url_rule('/coleccion', 'get_collection', AlbumController.get_collection, methods=['GET'])
api_bp.add_url_rule('/album/trade', 'trade_cards', AlbumController.trade_cards, methods=['POST'])

api_bp.add_url_rule('/tickets/available/<int:match_id>', 'get_available_tickets', TicketController.get_available_tickets, methods=['GET'])
api_bp.add_url_rule('/tickets/reserve', 'reserve_ticket', TicketController.reserve_ticket, methods=['POST'])
api_bp.add_url_rule('/tickets/purchase', 'purchase_ticket', TicketController.purchase_ticket, methods=['POST'])
api_bp.add_url_rule('/tickets/user/<string:user_id>', 'get_user_tickets', TicketController.get_user_tickets, methods=['GET'])

api_bp.add_url_rule('/shop/buy-pack', 'process_purchase', PaymentGatewayController.process_store_purchase, methods=['POST'])
api_bp.add_url_rule('/bet/place', 'place_bet', PaymentGatewayController.simulate_bet, methods=['POST'])