import 'package:flutter/material.dart';
void navigate(context,obj){
   Navigator.of(context).push(MaterialPageRoute(builder: (context) => obj,));
}