%global commitdate  20140204
%global commit      3d7767b6b1f3da363c625ff54e63bbf20e9e83ac
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora}
%global installdir  %{_jsdir}/json
%else
%global installdir  %{_datadir}/javascript/json
%endif

Name:            js-json
Version:         %{commitdate}git%{shortcommit}
Release:         13%{?dist}
Summary:         An implementation of JSON encoders/decoders in JavaScript

License:         Public Domain
URL:             https://github.com/douglascrockford/JSON-js
Source0:         https://github.com/douglascrockford/JSON-js/archive/%{commit}/%{name}-%{version}.tar.gz

BuildArch:       noarch

%if 0%{?fedora}
BuildRequires:   web-assets-devel
Requires:        web-assets-filesystem
%endif

%description
JSON is a light-weight, language independent, data interchange format.
See http://www.JSON.org/

This software is an implementation of JSON encoders/decoders in Javascript.

json2.js: This file creates a JSON property in the global object, if there
isn't already one, setting its value to an object containing a stringify
method and a parse method. The parse method uses the eval method to do the
parsing, guarding it with several regular expressions to defend against
accidental code execution hazards. On current browsers, this file does nothing,
preferring the built-in JSON object.

json.js: This file does everything that json2.js does. It also adds a
toJSONString method and a parseJSON method to Object.prototype. Use of this
file is not recommended.

json_parse.js: This file contains an alternative JSON parse function that
uses recursive descent instead of eval.

json_parse_state.js: This files contains an alternative JSON parse function that
uses a state machine instead of eval.

cycle.js: This file contains two functions, JSON.decycle and JSON.retrocycle,
which make it possible to encode cyclical structures and dags in JSON, and to
then recover them. JSONPath is used to represent the links.
http://GOESSNER.net/articles/JsonPath/


%prep
%setup -q -n JSON-js-%{commit}


%build
# nothing to do

%install
mkdir -p %{buildroot}%{installdir}
install -p -m0644 -D cycle.js \
    %{buildroot}%{installdir}/cycle.js
install -p -m0644 -D json.js \
    %{buildroot}%{installdir}/json.js
install -p -m0644 -D json2.js \
    %{buildroot}%{installdir}/json2.js
install -p -m0644 -D json_parse.js \
    %{buildroot}%{installdir}/json_parse.js
install -p -m0644 -D json_parse_state.js \
    %{buildroot}%{installdir}/json_parse_state.js


%files
%doc README
%{installdir}


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140204git3d7767b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140204git3d7767b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140204git3d7767b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 20140204git3d7767b-4
- move files to the correct location on EPEL 6

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 20140204git3d7767b-3
- add logic for building on EPEL 6

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 20140204git3d7767b-2
- install to %%{_jsdir}/json instead of %%{_jsdir}/js-json

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 20140204git3d7767b-1
- initial package

