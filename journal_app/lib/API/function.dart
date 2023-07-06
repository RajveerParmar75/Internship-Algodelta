import 'package:http/http.dart' as http;
const url = 'http://127.0.0.1:8000';
Future<http.Response> getAll() async {
  var res = await http.get(Uri.parse(url+'/add'));
  return res;
}
Future<http.Response> addUser(Map map) async {
  var res = await http.post(Uri.parse(url+'/add'),body: map);
  return res;
}
Future<http.Response> transaction(Map map) async {
  var res = await http.post(Uri.parse(url+'/transaction'),body: map);
  return res;
}
Future<http.Response> moneyAdd(Map map) async {
  var res = await http.patch(Uri.parse(url+'/add'),body: map);
  return res;
}
Future<http.Response> transection(int id) async {
  var res = await http.get(Uri.parse(url+'/transaction/$id'));
  return res;
}