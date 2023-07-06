import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:money_collection/database/database.dart';
import 'package:money_collection/database/model.dart';

class EditUser extends StatefulWidget {
  @override
  State<EditUser> createState() => _EditUserState();
}

class _EditUserState extends State<EditUser> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  TextEditingController _nameControllar = TextEditingController();
  TextEditingController _phoneControllar = TextEditingController();
  TextEditingController _addressControllar = TextEditingController();

  TextEditingController _loanControllar = TextEditingController();

  TextEditingController _outstandingController = TextEditingController();

  TextEditingController _penaltyController = TextEditingController();

  TextEditingController _daysController = TextEditingController();

  TextEditingController _typeController = TextEditingController();

  TextEditingController _startdateController = TextEditingController();

  TextEditingController _enddateController = TextEditingController();

  TextEditingController _documentController = TextEditingController();
  String _selectedFile = '';
  Future<void> _pickFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles();

    if (result != null) {
      String? filePath = result.files.single.path;
      if (filePath != null) {
        setState(() {
          _selectedFile = filePath;
        });
      }
    }
  }

  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      // Retrieve the form field values from the controllers
      String name = _loanControllar.text;
      String address = _outstandingController.text;
      int mobileNumber = int.parse(_penaltyController.text);
      num interest = num.parse(_daysController.text);
      String document = _typeController.text;
      print("$name $address   $document $mobileNumber $interest");
      // Perform any desired actions with the form data here
      myDatabase.edit(
          User.ConvertToUser(name, address, document, mobileNumber, interest),
          name: name);
      // Reset the form fields
      _formKey.currentState!.reset();
    }
  }

  String _selectedCategory = 'deposit';

  final List<String> _categories = ['deposit', 'withdraw'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _loanControllar,
                decoration: InputDecoration(labelText: 'name'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter loan amount';
                  }
                  return null;
                },
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _loanControllar,
                decoration: InputDecoration(labelText: 'address'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter loan amount';
                  }
                  return null;
                },
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _loanControllar,
                decoration: InputDecoration(labelText: 'mobile number'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter loan amount';
                  }
                  return null;
                },
              ),
              DropdownButtonFormField(
                value: _selectedCategory,
                onChanged: (value) {
                  setState(() {
                    _selectedCategory = value as String;
                  });
                },
                items: _categories.map((category) {
                  return DropdownMenuItem(
                    value: category,
                    child: Text(category),
                  );
                }).toList(),
                decoration: InputDecoration(),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please select a category';
                  }
                  return null;
                },
              ),
              SizedBox(height: 20.0),
              ElevatedButton(
                onPressed: _pickFile,
                child: Text('Upload Document'),
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _loanControllar,
                decoration: InputDecoration(labelText: 'loan amount'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter loan amount';
                  }
                  return null;
                },
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _outstandingController,
                decoration: InputDecoration(labelText: 'outstanding'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your outstanding';
                  }
                  return null;
                },
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _penaltyController,
                decoration: InputDecoration(labelText: 'penalty'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your penalty';
                  }
                  return null;
                },
              ),
              TextFormField(
                keyboardType: TextInputType.number,
                controller: _daysController,
                decoration: InputDecoration(labelText: 'days'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your loan days';
                  }
                  return null;
                },
              ),
              DropdownButtonFormField(
                value: _selectedCategory,
                onChanged: (value) {
                  setState(() {
                    _selectedCategory = value as String;
                  });
                },
                items: _categories.map((category) {
                  return DropdownMenuItem(
                    value: category,
                    child: Text(category),
                  );
                }).toList(),
                decoration: InputDecoration(),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please select a category';
                  }
                  return null;
                },
              ),
              TextField(
                controller: _startdateController,
                decoration: InputDecoration(
                  labelText: 'starting Date',
                  hintText: 'starting date',
                  prefixIcon: Icon(Icons.calendar_today),
                ),
                onTap: () async {
                  DateTime? pickedDate = await showDatePicker(
                    context: context,
                    initialDate: DateTime.now(),
                    firstDate: DateTime(2000),
                    lastDate: DateTime(2100),
                  );

                  if (pickedDate != null) {
                    setState(() {
                      _startdateController.text = pickedDate.toString();
                    });
                  }
                },
              ),
              SizedBox(height: 16.0),
              TextField(
                controller: _enddateController,
                decoration: InputDecoration(
                  labelText: 'end date',
                  hintText: 'end date',
                  prefixIcon: Icon(Icons.calendar_today),
                ),
                onTap: () async {
                  DateTime? pickedDate = await showDatePicker(
                    context: context,
                    initialDate: DateTime.now(),
                    firstDate: DateTime(2000),
                    lastDate: DateTime(2100),
                  );

                  if (pickedDate != null) {
                    setState(() {
                      _enddateController.text = pickedDate.toString();
                    });
                  }
                },
              ),
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: _submitForm,
                child: Text('Submit'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
