from rest_framework.views import APIView, status, Request, Response
from django.forms.models import model_to_dict
from teams.models import Team
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


class TeamView(APIView):
    def post(self, request: Request) -> Response:
        data = request.data
        try:
            data_processing(data)
        except (
            NegativeTitlesError,
            InvalidYearCupError,
            ImpossibleTitlesError,
        ) as error:
            return Response({"error": error.message}, status.HTTP_400_BAD_REQUEST)

        team_creat = Team.objects.create(**request.data)
        team_dict = model_to_dict(team_creat)
        return Response(team_dict, status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        teams = Team.objects.all()
        teams_dict = []
        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)
        return Response(teams_dict, status.HTTP_200_OK)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        team_dict = model_to_dict(found_team)
        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        found_team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request: Request, team_id) -> Response:
        try:
            found_team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        for k, v in request.data.items():
            setattr(found_team, k, v)
        found_team.save()
        team_dict = model_to_dict(found_team)
        return Response(team_dict, status.HTTP_200_OK)
