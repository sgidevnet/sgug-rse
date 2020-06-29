%global mod_name wtforms

Name:           python-wtforms
Version:        2.2.1
Release:        9%{?dist}
Summary:        Forms validation and rendering library for python

License:        BSD
URL:            http://wtforms.simplecodes.com/
Source0:        http://pypi.python.org/packages/source/W/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description\
With wtforms, your form field HTML can be generated for you.\
This allows you to maintain separation of code and presentation,\
and keep those messy parameters out of your python code.

%description %_description

%package -n python%{python3_pkgversion}-wtforms
Summary:        Forms validation and rendering library for python
%{?python_provide:%python_provide python3-wtforms}

%description -n python%{python3_pkgversion}-wtforms
With wtforms, your form field HTML can be generated for you. 
This allows you to maintain separation of code and presentation, 
and keep those messy parameters out of your python code.


%prep
%setup -q -n %{mod_name}-%{version}
sed -i "s|\r||g" docs/Makefile
sed -i "s|\r||g" CHANGES.rst
rm wtforms/locale/README.md

%build
%py3_build

%install
%py3_install
# rm -rf %{buildroot}/%{python3_sitelib}/wtforms/locale

#% find_lang wtforms

%files -n python%{python3_pkgversion}-wtforms
# -f wtforms.lang
%doc docs/ README.rst AUTHORS.rst  CHANGES.rst
%license LICENSE.rst
%{python3_sitelib}/WTForms-%{version}-py*.egg-info
%{python3_sitelib}/wtforms/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-7
- Subpackage python2-wtforms has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-2
- update some macros

* Sat Jun 30 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.2.1-1
- new version 2.2.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-15
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0-14
- make spec file compatible with epel7
- remove conditionals, always build for python 3

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0-11
- Python 2 binary package renamed to python2-wtforms
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-8
- Rebuild for Python 3.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec 01 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0-4
- Move the locale files into /usr/share/locale we will still have the same files
  present in both the py2 and py3 but a) they are completely identical so no
  conflicts from RPM and b) they are now in the proper place, system-wise

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fdoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat May 24 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 2.0-1
- Upgrade to upstream version
- Add python3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 09 2012 Tim Flink <tflink@fedoraproject.org> - 1.0.2-1
- Upgraded to upstream 1.0.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.6.3-1
- Initial RPM release
