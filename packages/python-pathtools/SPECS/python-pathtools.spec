%global upname pathtools

Name:		python-%{upname}
Version:	0.1.2
Release:	21%{?dist}
Summary:	Pattern matching and various utilities for file systems paths

License:	MIT
URL:		https://github.com/gorakhargosh/%{upname}
Source0:	%{pypi_source %{upname}}

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-sphinx
BuildRequires:	python3-flask-sphinx-themes

%global _description\
%{name} is a Python API library for common path\
and pattern functionality.\


%description %_description

%package -n python3-%{upname}
Summary: %summary
%{?python_provide:%python_provide python3-%{upname}}

%description -n python3-%{upname} %_description


%prep
%setup -qn %{upname}-%{version}

# remove hashbang from lib's files
sed -i -e '/#!\//d' pathtools/*.py


%build
%py3_build

pushd docs
make SPHINXBUILD=sphinx-build-3 html
rm -rf build/html/.build*
popd


%install
%py3_install


%files -n python3-%{upname}
%license LICENSE
%doc AUTHORS LICENSE README
%doc docs/build/html
%{python3_sitelib}/pathtools*/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-21
- Rebuilt for Python 3.9

* Mon Dec 09 2019 Stephen Coady <scoady@redhat.com> - 0.1.2-20
- Rebuilt to adopt package

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-19
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-18
- Drop python2-pathtools

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-16
- Only build the documentation on Python 3

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-14
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.2-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.2-11
- Python 2 binary package renamed to python2-pathtools
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 12 2013 Björn Esser <bjoern.esser@gmail.com> - 0.1.2-1
- Initial RPM release (#996088)
