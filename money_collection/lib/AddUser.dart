import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'package:money_collection/database/database.dart';
import 'package:money_collection/database/model.dart';

class AddUser extends StatefulWidget {
  @override
  State<AddUser> createState() => _AddUserState();
}

class _AddUserState extends State<AddUser> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  TextEditingController _nameController = TextEditingController();

  TextEditingController _addressController = TextEditingController();

  TextEditingController _mobileNumberController = TextEditingController();

  TextEditingController _interestController = TextEditingController();

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
      String name = _nameController.text,
          address = _addressController.text,
          document = _documentController.text;
      int mobileNumber = int.parse(_mobileNumberController.text);
      num interest = num.parse(_interestController.text);
      print("$name $address   $document $mobileNumber $interest");
      // Perform any desired actions with the form data here
      myDatabase.edit(
          User.ConvertToUser(name, address, document, mobileNumber, interest));
      // Reset the form fields
      _formKey.currentState!.reset();
    }
  }

  String _selectedCategory = 'Aadhar card';

  List<String> _categories = ['Pan card', 'Aadhar card'];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                controller: _nameController,
                decoration: InputDecoration(labelText: 'Name'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your name';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: _addressController,
                decoration: InputDecoration(labelText: 'Address'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your address';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: _mobileNumberController,
                decoration: InputDecoration(labelText: 'Mobile Number'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your mobile number';
                  }
                  return null;
                },
              ),
              TextFormField(
                controller: _interestController,
                decoration: InputDecoration(labelText: 'Interest'),
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Please enter your interest';
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
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: _pickFile,
                child: Text('Upload Document'),
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
