from django.http import JsonResponse

ERROR_CODES = {
	"OK": 0,
	"NOT REGISTERED": 1,
	"BAD EMAIL": 2,
	"NOT APPLICABLE": 3,
	"MISSING LINK": 4,

	"USER DELETED": 7,

	"IDENTITY ERROR": 8,
	"CREDENTIALS MISSING": 9,
	"DUPLICATE": 10,
	"BROKEN LINK": 11,
	"MALFORMED_JSON": 12,
	"PAYMENT_CALCULATION_ISSUE": 13,
	"CAPTCHA VERIFICATION FAILED": 14,
	"SESSION NOT FOUND": 15,
	"NOT SUBSCRIBED": 16,
	"ZERO LENGTH VIDEO": 17,
}

class JsonResponseMixin(object):
	@staticmethod
	def ok():
		return JsonResponse({"result": True, "message": "OK", "error_code": 0})

	@staticmethod
	def error(message):
		w(message)
		return JsonResponse({"result": False, "message": message, "error_code": ERROR_CODES.get(message, -1)})

	@staticmethod
	def serve_result(obj):
		obj.update({"result": True, "message": "OK", "error_code": 0})
		return JsonResponse(obj)

	@staticmethod
	def server_only_result(obj):
		return JsonResponse(obj)
