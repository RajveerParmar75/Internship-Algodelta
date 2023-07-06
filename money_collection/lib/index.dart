// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:money_collection/AddUser.dart';
import 'package:money_collection/DetailUser.dart';
import 'package:money_collection/database/database.dart';
import 'package:money_collection/database/model.dart';
import 'package:money_collection/style.dart';

class Index extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        appBar: AppBar(
            title: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text("Saving "),
                Text("loan"),
              ],
            ),
            centerTitle: true),
        body: SingleChildScrollView(
          scrollDirection: Axis.vertical,
          child: InkWell(
            onTap: () async {
              navigate(context, DetailUser(await myDatabase.fetchData()));
            },
            child: Card(
              child: Padding(
                padding: EdgeInsets.all(16.0),
                child: Row(
                  children: [
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text("100" + ' ₹',
                              style: TextStyle(
                                  fontSize: 25,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.blue.shade600)),
                          SizedBox(height: 8.0),
                          Text("rajveer", style: TextStyle(fontSize: 25)),
                        ],
                      ),
                    ),
                    SizedBox(width: 16.0),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text("100" + ' ₹',
                            style: TextStyle(
                                fontSize: 25,
                                fontWeight: FontWeight.bold,
                                color: Colors.red)),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
        floatingActionButton: Stack(
          children: [
            Padding(
              padding: const EdgeInsets.only(left: 25.0),
              child: Align(
                alignment: Alignment.bottomLeft,
                child: FloatingActionButton(
                  heroTag: "add user",
                  onPressed: () {
                    navigate(context, AddUser());
                  },
                  child: Icon(Icons.add),
                ),
              ),
            ),
            Align(
              alignment: Alignment.bottomRight,
              child: FloatingActionButton(
                heroTag: "notify user",
                onPressed: () {},
                child: Icon(Icons.notification_add_outlined),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
