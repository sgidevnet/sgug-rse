%{?python_enable_dependency_generator}
%global srcname fontname

Name:           python-fontname
Version:        0.2.0
Release:        20%{?dist}
Summary:        A lib for guessing font name

License:        MIT
URL:            https://github.com/Asvel/fontname
Source0:        https://pypi.python.org/packages/source/f/%{srcname}/%{srcname}-%{version}.zip

BuildArch:      noarch

%global _description\
fontname is a lib for guessing font name, in other words, reading and decoding\
quirk encoded raw font name.\
\
It current supports SFNT format fonts, and is adept at dealing with CJK fonts.

%description %_description

%package -n python3-%{srcname}
Summary:        A lib for guessing font name
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-freetype
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
fontname is a lib for guessing font name, in other words, reading and decoding
quirk encoded raw font name.

It current supports SFNT format fonts, and is adept at dealing with CJK fonts.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc PKG-INFO README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/__pycache__/%{srcname}*
%{python3_sitelib}/%{srcname}-%{version}-py3.*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Parag Nemade <pnemade AT redhat DOT com> - 0.2.0-14
- Resolves:rh#1629797 - Remove python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-12
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.0-9
- Python 2 binary package renamed to python2-fontname
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.2.0-4
- Enabled python3 subpackage and rewrote spec for new python guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 31 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.2.0-2
- Follow python3 subpackage guidelines
- Add python3-freetype to python3-fontname subpackage

* Mon Sep 22 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.2.0-1
- Initial packaging

