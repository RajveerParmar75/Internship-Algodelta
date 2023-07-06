import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:journal_app/API/function.dart';
import 'package:journal_app/DetailUser.dart';
import 'package:journal_app/AddUser.dart';
import 'package:http/http.dart' as http;

class Indexpage extends StatefulWidget {
  @override
  State<Indexpage> createState() => _IndexpageState();
}

class _IndexpageState extends State<Indexpage> {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.blue,
          centerTitle: true,
          title: Text(
            'USERS',
            style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
          ),
        ),
        body: SingleChildScrollView(
          child: FutureBuilder<http.Response>(
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  Map<String, dynamic> data = jsonDecode(snapshot.data!.body);
                  return ListView.builder(
                    itemCount: data['data'].length,
                    shrinkWrap: true,
                    itemBuilder: (context, index) {
                      return Center(
                        child: InkWell(
                          onTap: () {
                            Navigator.push(
                              context,
                              MaterialPageRoute(
                                  builder: (context) =>
                                      DetailUser(data['data'][index])),
                            );
                          },
                          child: Card(
                            margin: EdgeInsets.all(20.0),
                            child: Padding(
                              padding: EdgeInsets.all(16.0),
                              child: Column(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Text(
                                    '${data['data'][index]['name']}',
                                    style: TextStyle(
                                      fontSize: 20.0,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  SizedBox(
                                      height: 10.0, width: double.infinity),
                                  Text(
                                    '${data['data'][index]['contact_number']}',
                                    style: TextStyle(fontSize: 14.0),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      );
                    },
                  );
                } else {
                  return Center(child: CircularProgressIndicator());
                }
              },
              future: getAll()),
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(
                builder: (context) => AddUser(),
              ),
            ).then((value) {
              setState(() {});
            });
          },
          tooltip: 'Add Data',
          child: Icon(Icons.add),
        ),
      ),
    );
  }
}
