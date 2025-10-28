# Finance Service - YFinance Microservice

Microserviço performático baseado em FastAPI que fornece dados financeiros usando a biblioteca yfinance.

## 🚀 Execução

### Usando Docker Compose

```bash
cd finance-service
docker-compose up -d
```

### Execução Local

```bash
cd finance-service
pip install -r requirements.txt
python main.py
```

O serviço estará disponível em: `http://localhost:8000`

## 📚 API Endpoints

### Health Check
- **GET** `/health` - Status do serviço

### Ticker Endpoints
- **POST** `/ticker/info` - Informações completas da ação
- **POST** `/ticker/fast-info` - Informações rápidas da ação
- **POST** `/ticker/history` - Histórico de preços
- **POST** `/ticker/recommendations` - Recomendações de analistas
- **POST** `/ticker/news` - Notícias da ação
- **POST** `/ticker/earnings` - Histórico de lucros
- **POST** `/ticker/financials` - Demonstrações financeiras
- **POST** `/ticker/balance-sheet` - Balanço patrimonial
- **POST** `/ticker/cashflow` - Fluxo de caixa
- **POST** `/ticker/dividends` - Histórico de dividendos
- **POST** `/ticker/splits` - Histórico de splits
- **POST** `/ticker/actions` - Ações corporativas

### Market Endpoints
- **POST** `/market/download` - Download de múltiplas ações
- **GET** `/market/search/{query}` - Buscar ações

## 📝 Exemplos de Uso

### Buscar informações de uma ação
```bash
curl -X POST "http://localhost:8000/ticker/info" \
     -H "Content-Type: application/json" \
     -d '{"symbol": "AAPL"}'
```

### Obter histórico de preços
```bash
curl -X POST "http://localhost:8000/ticker/history" \
     -H "Content-Type: application/json" \
     -d '{"symbol": "AAPL", "period": "1y", "interval": "1d"}'
```

### Buscar ações
```bash
curl "http://localhost:8000/market/search/Apple"
```

## 🔧 Configuração

### Variáveis de Ambiente
- `HOST`: Host do serviço (padrão: 0.0.0.0)
- `PORT`: Porta do serviço (padrão: 8000)

## 📋 Estrutura do Projeto

```
finance-service/
├── app/
│   ├── core/
│   │   └── config.py          # Configurações
│   ├── routers/
│   │   ├── ticker.py          # Endpoints de ações
│   │   └── market.py          # Endpoints de mercado
│   ├── schemas/
│   │   └── requests.py        # Modelos Pydantic
│   └── services/
│       └── yfinance_service.py # Lógica de negócio
├── main.py                    # Entrada da aplicação
├── requirements.txt           # Dependências
├── Dockerfile                 # Container Docker
└── docker-compose.yml         # Orquestração
```

## 🌐 Integração com NextJS

Use a biblioteca `lib/finance-service.ts` no projeto NextJS para comunicar com este microserviço.

Exemplo:
```typescript
import { financeService } from '@/lib/finance-service'

const stockInfo = await financeService.getTickerInfo('AAPL')