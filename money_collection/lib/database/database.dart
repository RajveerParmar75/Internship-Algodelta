import 'dart:io';
import 'package:flutter/services.dart';
import 'package:money_collection/database/model.dart';
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

final MyDatabase myDatabase = MyDatabase();

class MyDatabase {
  final String _name = 'name',
      _address = 'address',
      _document = 'document',
      _phoneNo = 'phoneNo',
      _interest = 'interest';
  Future<Database> initDatabase() async {
    Directory appDocDir = await getApplicationDocumentsDirectory();
    String databasePath = join(appDocDir.path, 'money_collections.db');
    return await openDatabase(databasePath);
  }

  Future<bool> copyPasteAssetFileToRoot() async {
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    String path = join(documentsDirectory.path, "money_collections.db");

    if (FileSystemEntity.typeSync(path) == FileSystemEntityType.notFound) {
      ByteData data = await rootBundle
          .load(join('assets/database', 'money_collections.db'));
      List<int> bytes =
          data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes);
      await File(path).writeAsBytes(bytes);
      return true;
    }
    return false;
  }

  Future<void> delete(String name) async {
    Database database = await initDatabase();
    await database.rawDelete('DELETE FROM User WHERE name = $name');
  }

  Future<List<User>> fetchData({String? name}) async {
    List<User> listUser = [];
    Database database = await initDatabase();
    List<Map> data = await database.rawQuery(
        'select * from User ${name != null ? ('where name=${name}') : ''}');
    for (var element in data) {
      listUser.add(User(element[_name], element[_address], element[_phoneNo],
          element[_interest], element[_document]));
    }
    print(listUser);
    return listUser;
  }

  Future<void> edit(Map<String, dynamic> element, {String? name}) async {
    Database database = await initDatabase();
    if (name != null) {
      await database.rawInsert(
          'INSERT INTO User($_name,$_address,$_document,$_phoneNo,$_interest) VALUES("${element[_name]}", "${element[_address]}", "${element[_document]}", ${element[_phoneNo]}, ${element[_interest]})');
    } else {
      await database.rawUpdate(
          'UPDATE User SET name = ${element[_name]}, address = "${element[_address]}", document = "${element[_document]}", phoneNo= ${element[_phoneNo]}, interest = "${element[_interest]}", WHERE name = $name');
    }
  }
}
