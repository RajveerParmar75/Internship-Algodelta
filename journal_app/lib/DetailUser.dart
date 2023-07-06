import 'package:flutter/material.dart';
import 'package:flutter_dialogs/flutter_dialogs.dart';
import 'package:journal_app/API/function.dart';
import 'package:journal_app/Log.dart';

class DetailUser extends StatelessWidget {
  Map map = {};
  final TextEditingController _amountController = TextEditingController();

  DetailUser(this.map) {}

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          icon: Icon(Icons.arrow_back_ios_new),
        ),
        centerTitle: true,
        title: const Text('details '),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Hero(
              tag: 'nameHero',
              child: Text(
                '${map['name']}',
                style: TextStyle(
                  fontSize: 36.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            SizedBox(height: 16.0),
            Text(
              '${map['contact_number']}',
              style: TextStyle(fontSize: 16.0),
            ),
            SizedBox(height: 32.0),
            Card(
              child: SizedBox(
                height: 200.0,
                width: 200.0,
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(
                      '₹${map['money']}',
                      style: TextStyle(
                        fontSize: 24.0,
                        fontWeight: FontWeight.bold,
                        color: Colors.blue,
                      ),
                    ),
                    Text(
                      'PAYMENT',
                      style: TextStyle(
                        fontSize: 18.0,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
      floatingActionButton: Stack(
        children: [
          Padding(
            padding: const EdgeInsets.only(left: 25.0),
            child: Align(
              alignment: Alignment.bottomLeft,
              child: FloatingActionButton(
                heroTag: "hello",
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => Transection(map['id']),
                    ),
                  );
                },
                child: Icon(Icons.history),
              ),
            ),
          ),
          Align(
            alignment: Alignment.bottomRight,
            child: FloatingActionButton(
              heroTag: "data",
              onPressed: () {
                showDialog(
                  context: context,
                  builder: (BuildContext context) {
                    return AlertDialog(
                      title: const Text('MONEY'),
                      content: Column(
                        children: [
                          Text('Choose an option:'),
                          SizedBox(height: 16.0),
                          TextField(
                            controller: _amountController,
                            decoration: InputDecoration(
                              labelText: 'Amount',
                            ),
                          ),
                        ],
                      ),
                      actions: [
                        ElevatedButton(
                          child: Text('Credit'),
                          onPressed: () {
                            // Add your credit logic her
                            print(map['id']);
                            String amount = _amountController.text;
                            moneyAdd(
                              {
                                "flag": "credit",
                                "money": amount,
                                "id": map['id'].toString()
                              },
                            ).then(
                              (value) => {
                                Navigator.of(context).pop(),
                                Navigator.of(context).pop()
                              },
                            );
                          },
                        ),
                        ElevatedButton(
                          child: Text('Debit'),
                          onPressed: () {
                            // Add your debit logic here
                            String amount = _amountController.text;
                            moneyAdd({
                              "flag": "debit",
                              "money": amount,
                              "id": map['id'].toString()
                            }).then((value) => {
                                  Navigator.of(context).pop(),
                                  Navigator.of(context).pop()
                                });
                          },
                        ),
                      ],
                    );
                  },
                );
              },
              child: Icon(Icons.add),
            ),
          ),
        ],
      ),
    );
  }
}
