import 'package:flutter/material.dart';
import 'package:money_collection/EditUser.dart';
import 'package:money_collection/UserLoan.dart';
import 'package:money_collection/database/database.dart';
import 'package:money_collection/database/model.dart';
import 'package:money_collection/style.dart';

class DetailUser extends StatelessWidget {
  List<User> users;

  DetailUser(this.users);
  List<Text> displayUser() {
    List<Text> txt = [];
    for (User data in users) {
      txt.add(Text(
          'Name: ${data.name}, Address: ${data.address}, Phone no: ${data.phoneNo}, Interest: ${data.interest}, document: ${data.document}, '));
    }
    return txt;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ...displayUser(),
                Text(
                  'Name: John Doe',
                  style: TextStyle(
                      fontSize: 32,
                      fontWeight: FontWeight.bold,
                      color: Colors.cyan),
                ),
              ],
            ),
            SizedBox(height: 30),
            Text(
              'Mobile: 555-1234',
              style: TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                  color: Colors.black26),
            ),
            SizedBox(height: 30),
            Text(
              'Address: 123 Main Street',
              style: TextStyle(
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                  color: Colors.black26),
            ),
            SizedBox(height: 16),
            Card(
              color: Colors.purple.shade50,
              margin: EdgeInsets.all(16),
              child: Padding(
                padding: EdgeInsets.all(16),
                child: Center(
                  child: Text(
                    'Transaction',
                    style: TextStyle(
                        fontSize: 24,
                        color: Colors.black54,
                        fontWeight: FontWeight.bold),
                  ),
                ),
              ),
            ),
            InkWell(
              onTap: () {
                navigate(context, UserLoan());
              },
              child: Card(
                color: Colors.purple.shade50,
                margin: EdgeInsets.all(16),
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: Center(
                    child: Text(
                      'Add loan',
                      style: TextStyle(
                          fontSize: 24,
                          color: Colors.black54,
                          fontWeight: FontWeight.bold),
                    ),
                  ),
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(width: 16),
              ],
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        heroTag: "add user",
        onPressed: () {
          navigate(context, EditUser());
        },
        child: Icon(Icons.edit),
      ),
    );
  }
}
