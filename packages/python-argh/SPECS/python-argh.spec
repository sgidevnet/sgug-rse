%global pypi_name argh
%global global_sum Unobtrusive argparse wrapper with natural syntax
%global global_desc							\
Building a command-line interface?  Found yourself uttering “argh!”	\
while struggling with the API of argparse?  Don’t want to lose its	\
power but don’t need the complexity?					\
									\
%{name} provides a wrapper for argparse.  Argparse is a very powerful	\
tool;  %{name} just makes it easy to use.


Name:		python-%{pypi_name}
Version:	0.26.1
Release:	17%{?dist}
Summary:	%{global_sum}

License:	LGPLv3+
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	%{pypi_source}
Source1:	https://www.gnu.org/licenses/lgpl-3.0.txt
Source2:	https://www.gnu.org/licenses/gpl-3.0.txt

# not upstreamed, fixes an assert in testsuite.
Patch0001:	python-argh-0.26.1-fix-testsuite.patch

BuildArch:	noarch
BuildRequires:  glibc-langpack-en

%description
%{global_desc}


%package -n python3-%{pypi_name}
Summary:	%{global_sum}

BuildRequires:	python3-devel
BuildRequires:	python3-mock
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{global_desc}


%prep
%autosetup -n %{pypi_name}-%{version} -p 1

%{__install} -pm 0644 %{SOURCE1} COPYING
%{__install} -pm 0644 %{SOURCE2} .


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%doc README.rst
%license COPYING gpl-3.0.txt
%{python3_sitelib}/argh*/


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-14
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-13
- Drop python2-argh

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.26.1-11
- Add BR:glibc-langpack-en
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-9
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.26.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Björn Esser <besser82@fedoraproject.org> - 0.26.1-5
- Adapt spec-file to recent guidelines

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 20 2016 Miro Hrončok <mhroncok@redhat.com> - 0.26.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 08 2016 Björn Esser <fedora@besser82.io> - 0.26.1-1
- new upstream-release (#1301580)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.23.2-5
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Aug 12 2013 Björn Esser <bjoern.esser@gmail.com> - 0.23.2-1
- Initial rpm release (#996186)
