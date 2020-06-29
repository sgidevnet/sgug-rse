%global srcname tambo

Name:           python-%{srcname}
Version:        0.4.0
Release:        15%{?dist}
Summary:        A command line object dispatcher

License:        MIT
URL:            https://github.com/alfredodeza/tambo

Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%global _description\
Use any argument parser you want for each sub-command. Easily manage each\
command as a self-contained application.

%description %_description

%package -n python3-tambo
Summary:        A command line object dispatcher
Requires:       python3

%description -n python3-tambo
Use any argument parser you want for each sub-command. Easily manage each
command as a self-contained application.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# Upstream accidentally included this stale cache. Delete it.
rm -r tambo/tests/__pycache__/


%build
%py3_build

%install
%py3_install

%check
py.test-%{python3_version} -v tambo/tests

%files -n python3-tambo
%{python3_sitelib}/*
%license LICENSE
%doc README.rst


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Ken Dreyer <kdreyer@redhat.com> - 0.4.0-10
- Use standard %%srcname macro
- Use %%pypi_source macro for Source0
- Drop PYTHONPATH manipulation in %%check

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-8
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-3
- Python 2 binary package renamed to python2-tambo
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Ken Dreyer <ktdreyer@ktdreyer.com> 0.4.0-1
- Update to 0.4.0 (rhbz#1464677)
- Use %%autosetup macro

* Wed May 10 2017 Ken Dreyer <ktdreyer@ktdreyer.com> 0.3.0-1
- Update to 0.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.2.0-4
- Drop BR: python-mock (the test suites no longer depend on this)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.2.0-1
- Update to latest upstream version (rhbz#1273020)

* Fri Sep 25 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.1.0-1
- Update to latest upstream version

* Sat Jun 27 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.9-2
- set _docdir_fmt to get the same license and doc directories for python- and
  python3- subpackages (rhbz#1208665)

* Thu Apr 02 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.0.9-1
- Initial package
