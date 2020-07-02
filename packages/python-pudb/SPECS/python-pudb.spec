# Enable Python dependency generation
%{?python_enable_dependency_generator}

%global upstream_name pudb
%global module_name pudb

Name:          python-pudb
Version:       2017.1.4
Release:       10%{?dist}
Summary:       A full-screen, console-based Python debugger
License:       MIT
URL:           http://mathema.tician.de/software/pudb
Source0:       https://files.pythonhosted.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%global _description\
PuDB is a full-screen, console-based visual debugger for Python.\
\
Its goal is to provide all the niceties of modern GUI-based debuggers in a more\
lightweight and keyboard-friendly package. PuDB allows you to debug code right\
where you write and test it--in a terminal. If you've worked with the excellent\
(but nowadays ancient) DOS-based Turbo Pascal or C tools, PuDB's UI might look\
familiar.

%description %_description

%package -n python3-%{upstream_name}
Summary:       A full-screen, console-based Python debugger
%{?python_provide:%python_provide python3-%{upstream_name}}

%description -n python3-%{upstream_name} %_description


%prep
%setup -q -n %{upstream_name}-%{version}
rm -rf %{module_name}.egg-info

sed -i '1{\@^#! /usr/bin/env python@d}' pudb/debugger.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{upstream_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{module_name}
%{python3_sitelib}/%{module_name}*.egg-info
%{_bindir}/pudb3

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-5
- Removed python2-pudb (#1701957)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.1.4-2
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Neal Gompa <ngompa13@gmail.com> - 2017.1.4-1
- Rebase to pudb-2017.1.4
- Clean up spec

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2015.3-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2015.3-8
- Python 2 binary package renamed to python2-pudb
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Oct 14 2015 Dhiru Kholia <dhiru@openwall.com> - 2015.3-1
- update to pudb-2015.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2014.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sat Mar 15 2014 Dhiru Kholia <dhiru@openwall.com> - 2014.1-1
- update to pudb-2014.1

* Mon Dec 09 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.5.1-1
- update to pudb-2013.5.1

* Wed Nov 13 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.4-1
- update to pudb-2013.4

* Tue Sep 10 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.6-2
- replaced {python_sitelib} with {python2_sitelib}

* Fri Sep 06 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.6-1
- update to upstream release 2013.3.6

* Fri Sep 06 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-5
- replaced {__python} with {__python2}

* Thu Sep 05 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-4
- make layout of install section consistent with that of build section

* Thu Sep 05 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-3
- removed the unnecessary attr directive
- fixed the location of the sed command invocation

* Thu Sep 05 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-2
- implemented initial fixes suggested in BZ #1004257
- removed unused EL5 support, removed invalid BuildRoot, fixed BuildRequires

* Wed Sep 04 2013 Dhiru Kholia <dhiru@openwall.com> - 2013.3.5-1
- initial version
