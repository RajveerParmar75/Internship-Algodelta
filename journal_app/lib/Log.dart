import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:journal_app/API/function.dart';

class Transection extends StatelessWidget {
  int id;

  Transection(this.id);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Transection"), centerTitle: true),
      body: FutureBuilder(
        future: transection(id),
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            Map<String, dynamic> map = jsonDecode(snapshot.data!.body);
            print(map['data']);
            return ListView.builder(
              itemCount: map['data'].length,
              itemBuilder: (context, index) {
                return Card(
                  child: Padding(
                    padding: EdgeInsets.all(16.0),
                    child: Row(
                      children: [
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Amount',
                                style: TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 18.0,
                                ),
                              ),
                              SizedBox(height: 8.0),
                              Text(
                                map['data'][index]['is_credited']
                                    ? "+${map['data'][index]['money']}"
                                    : "-${map['data'][index]['money']}",
                                style: TextStyle(fontSize: 16.0),
                              ),
                            ],
                          ),
                        ),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Date',
                                style: TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 18.0,
                                ),
                              ),
                              SizedBox(height: 8.0),
                              Text(
                                map['data'][index]['date']
                                    .toString()
                                    .substring(0, 10),
                                style: TextStyle(fontSize: 16.0),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            );
          } else {
            return Center(child: CircularProgressIndicator());
          }
        },
      ),
    );
  }
}
