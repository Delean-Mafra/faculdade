# api_v1/views.py (Exemplo para Simulação)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SimulacaoRequestSerializer, SimulacaoResponseSerializer
class SimularApoliceAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SimulacaoRequestSerializer(data=request.data)
        if serializer.is_valid():
            idade = serializer.validated_data['idade']
            valor_veiculo = serializer.validated_data['valorVeiculo']
            historico = serializer.validated_data['historico']

            taxa_base = 0.05
            fator_historico = 1.1 if historico == 'com_sinistros' else 1.0
            valor_final = float(valor_veiculo) * taxa_base * fator_historico
            desconto_str = "0%"

            if idade >= 60:
                desconto = 0.20
                valor_final *= (1 - desconto)
                desconto_str = "20%"

            response_data = {'valorSeguro': round(valor_final, 2), 'descontoAposentado': desconto_str}
            response_serializer = SimulacaoResponseSerializer(response_data)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
