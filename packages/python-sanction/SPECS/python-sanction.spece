
%global modname sanction

Name:               python-sanction
Version:            0.3.1
Release:            23%{?dist}
Summary:            A simple, lightweight OAuth2 client
License:            MIT
URL:                http://pypi.python.org/pypi/sanction
Source0:            http://pypi.python.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-nose


%global _description\
python-sanction is a lightweight, dead simple client implementation of\
the OAuth2 protocol.\
\
- Variations on OAuth2 client implementation range from a few hundred LOC\
  to thousands. In a Pythonic world, there's absolutely no need for this when\
  simply dealing with the client side of the spec. Currently, sanction sits\
  at a whopping 65 LOC, one class. This makes the library tremendously easy\
  to grok.\
\
- Most providers have varying levels of diversion from the official spec.\
  The goal with this library is to either handle these diversions natively,\
  or expose a method to allow client code to deal with it efficiently and\
  effectively.\
\
- Three of the four OAuth2 flows should be supported by this library.\
  Currently, only authorization code and client credential flows have been\
  tested due to lack of other (known) implementations.\
\
sanction has been tested with the following OAuth2 providers:\
\
* Facebook (include the test API)\
* Google\
* Foursquare\
* bitly\
* GitHub\
* StackExchange\
* Instagram\
* DeviantArt

%description %_description

%package -n python3-sanction
Summary:            A simple, lightweight OAuth2 client

%description -n python3-sanction
python-sanction is a lightweight, dead simple client implementation of
the OAuth2 protocol.

- Variations on OAuth2 client implementation range from a few hundred LOC
  to thousands. In a Pythonic world, there's absolutely no need for this when
  simply dealing with the client side of the spec. Currently, sanction sits
  at a whopping 65 LOC, one class. This makes the library tremendously easy
  to grok.

- Most providers have varying levels of diversion from the official spec.
  The goal with this library is to either handle these diversions natively,
  or expose a method to allow client code to deal with it efficiently and
  effectively.

- Three of the four OAuth2 flows should be supported by this library.
  Currently, only authorization code and client credential flows have been
  tested due to lack of other (known) implementations.

sanction has been tested with the following OAuth2 providers:

* Facebook (include the test API)
* Google
* Foursquare
* bitly
* GitHub
* StackExchange
* Instagram
* DeviantArt


%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=$(pwd) nosetests-%{python3_version}

%files -n python3-sanction
%doc README.rst LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-23
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-21
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-20
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.1-17
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.3.1-16
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-14
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.1-11
- Python 2 binary package renamed to python2-sanction
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Oct 07 2013 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- Latest upstream.
- Added python3 subpackage.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 04 2013 Ralph Bean <rbean@redhat.com> - 0.1.4-1
- Initial packaging for Fedora
