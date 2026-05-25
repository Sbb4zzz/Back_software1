from flask import jsonify
from datetime import datetime, timezone
from models.match import MatchModel
from services.api_service import FootballAPIService
import logging, requests

logger = logging.getLogger(__name__)


class MatchController:

    @staticmethod
    def get_matches():
        try:
            data = FootballAPIService.get_world_cup_matches()

            return jsonify({
                "source": "world-cup-api",
                "total": len(data.get("matches", [])),
                "partidos": data.get("matches", [])
            }), 200

        except Exception as e:
            logger.error(f"Error API mundial: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def get_match_by_id(match_id):
        try:
            partido = MatchModel.get_match_by_id(match_id)

            if not partido:
                return jsonify({"error": "Partido no encontrado"}), 404

            return jsonify(partido), 200

        except Exception as e:
            logger.error(str(e))
            return jsonify({"error": str(e)}), 500


    @staticmethod
    def get_matches_by_phase(phase):
        data = FootballAPIService.get_world_cup_matches()

        matches = [
            m for m in data.get("matches", [])
            if m.get("stage") == phase
        ]

        return jsonify({"matches": matches}), 200
    
    @staticmethod
    def get_live_matches():
        try:
            data = FootballAPIService.get_world_cup_matches()

            live = [
                m for m in data.get("matches", [])
                if m.get("status") == "IN_PLAY"
            ]

            return jsonify({
                "source": "world-cup-api",
                "live_matches": live
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500


    from datetime import datetime

    @staticmethod
    def get_today_matches():
        data = FootballAPIService.get_world_cup_matches()

        today = datetime.utcnow().date()

        matches = [
            m for m in data.get("matches", [])
            if m.get("utcDate", "")[:10] == str(today)
        ]

        return jsonify({"matches": matches}), 200
        
    @staticmethod
    def get_matches_by_group(group):
        data = FootballAPIService.get_world_cup_matches()

        matches = [
            m for m in data.get("matches", [])
            if m.get("group") == f"GROUP_{group.upper()}"
        ]

        return jsonify({"matches": matches}), 200
 
    @staticmethod
    def get_standings():
        try:
            data = FootballAPIService.get_world_cup_standings()

            return jsonify({
                "source": "world-cup-api",
                "standings": data.get("standings", [])
            }), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500