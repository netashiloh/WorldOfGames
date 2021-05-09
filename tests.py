# from openexchangerate import OpenExchangeRates

# client = OpenExchangeRates(api_key="873650114a6e43e8b46644757901d1fc")
# latest_conversions = (client.latest()[0])

latest_conversions = {'AED': 3.6732, 'AFN': 76.887345, 'ALL': 101.086542, 'AMD': 517.517805, 'ANG': 1.781514, 'AOA': 654.1125,
              'ARS': 93.088278, 'AUD': 1.274673, 'AWG': 1.80025, 'AZN': 1.700805, 'BAM': 1.607983, 'BBD': 2.0,
              'BDT': 84.106465, 'BGN': 1.607958, 'BHD': 0.37416, 'BIF': 1960.395019, 'BMD': 1.0, 'BND': 1.321357,
              'BOB': 6.843073, 'BRL': 5.236512, 'BSD': 1.0, 'BTC': 1.7339184e-05, 'BTN': 72.90296, 'BWP': 10.787742,
              'BYN': 2.514624, 'BZD': 2.000534, 'CAD': 1.21356, 'CDF': 1975.171503, 'CHF': 0.901224, 'CLF': 0.025202,
              'CLP': 695.4, 'CNH': 6.416865, 'CNY': 6.4325, 'COP': 3775.30675, 'CRC': 611.90074, 'CUC': 1.0,
              'CUP': 25.75, 'CVE': 91.2, 'CZK': 21.07625, 'DJF': 176.679766, 'DKK': 6.1132, 'DOP': 56.431469,
              'DZD': 133.408421, 'EGP': 15.670976, 'ERN': 15.00197, 'ETB': 41.874251, 'EUR': 0.822149,
              'FJD': 2.0276, 'FKP': 0.715589, 'GBP': 0.715589, 'GEL': 3.425, 'GGP': 0.715589, 'GHS': 5.726513,
              'GIP': 0.715589, 'GMD': 51.2, 'GNF': 9796.718583, 'GTQ': 7.656835, 'GYD': 207.6419, 'HKD': 7.76588,
              'HNL': 23.820114, 'HRK': 6.195055, 'HTG': 86.592807, 'HUF': 294.68, 'IDR': 14131.5, 'ILS': 3.240006,
              'IMP': 0.715589, 'INR': 73.296, 'IQD': 1448.007928, 'IRR': 42105.0, 'ISK': 123.73339, 'JEP': 0.715589,
              'JMD': 150.805084, 'JOD': 0.709, 'JPY': 108.585, 'KES': 105.94561, 'KGS': 84.786202, 'KHR': 4019.502631,
              'KMF': 404.749815, 'KPW': 900.0, 'KRW': 1112.97, 'KWD': 0.298604, 'KYD': 0.827082, 'KZT': 423.389951,
              'LAK': 9353.900674, 'LBP': 1496.635429, 'LKR': 195.515584, 'LRD': 172.0, 'LSL': 14.101424,
              'LYD': 4.456868, 'MAD': 8.809981, 'MDL': 17.803193, 'MGA': 3749.321772, 'MKD': 50.656694,
              'MMK': 1545.761635, 'MNT': 2850.826192, 'MOP': 7.939983, 'MRO': 356.999828, 'MRU': 35.748669,
              'MUR': 40.702291, 'MVR': 15.35, 'MWK': 787.521067, 'MXN': 19.9081, 'MYR': 4.1125, 'MZN': 58.099999,
              'NAD': 14.06, 'NGN': 405.673021, 'NIO': 34.66179, 'NOK': 8.2186, 'NPR': 116.644815, 'NZD': 1.373344,
              'OMR': 0.385012, 'PAB': 1.0, 'PEN': 3.789694, 'PGK': 3.529402, 'PHP': 47.526202, 'PKR': 150.93405,
              'PLN': 3.74255, 'PYG': 6760.278882, 'QAR': 3.61359, 'RON': 4.0503, 'RSD': 96.68467, 'RUB': 73.71914,
              'RWF': 993.409703, 'SAR': 3.750376, 'SBD': 7.964986, 'SCR': 14.936, 'SDG': 402.0, 'SEK': 8.30775,
              'SGD': 1.3246, 'SHP': 0.715589, 'SLL': 10223.75017, 'SOS': 574.10567, 'SRD': 14.154, 'SSP': 130.26,
              'STD': 20738.069016, 'STN': 20.55, 'SVC': 8.684356, 'SYP': 1257.639136, 'SZL': 14.120556,
              'THB': 31.041868, 'TJS': 11.319096, 'TMT': 3.51, 'TND': 2.7425, 'TOP': 2.258677, 'TRY': 8.2371,
              'TTD': 6.743428, 'TWD': 27.659961, 'TZS': 2301.51938, 'UAH': 27.547161, 'UGX': 3530.219639,
              'USD': 1.0, 'UYU': 43.886646, 'UZS': 10414.223156, 'VES': 2591296.49, 'VND': 22891.085938,
              'VUV': 109.544432, 'WST': 2.531864, 'XAF': 539.294195, 'XAG': 0.03642992, 'XAU': 0.00054602,
              'XCD': 2.70255, 'XDR': 0.694374, 'XOF': 539.294195, 'XPD': 0.00034135, 'XPF': 98.108437,
              'XPT': 0.00079531, 'YER': 250.400036, 'ZAR': 14.062555, 'ZMW': 22.202455, 'ZWL': 322.0}

ILS_value = latest_conversions['ILS']


secret = 3.240006