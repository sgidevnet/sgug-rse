%global modname q

Name:           python-%{modname}
Version:        2.6
Release:        17%{?dist}
Summary:        Quick and dirty python debugging output

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/q
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz
# https://github.com/zestyping/q/pull/28
Patch0001:      0001-Alternate-pprint-for-values.patch

BuildArch:      noarch

%global _description \
If you have ever been frustrated trying to debug with print because a web\
application or a unittesting framework is swallowing your debugging output,\
q will make you jump for joy.\
\
  import q\
  variable = 'Hmmm... something happened here'\
  q.q(variable)\
\
cat /tmp/q

%description %{_description}


%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
%{__python3} test/test_*.py -v

%files -n python3-%{modname}
%doc README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.6-17
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-15
- Subpackage python2-q has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.6-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.6-10
- Deal with rpm's inability to replace directories with files

* Tue Sep 18 2018 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.6-9
- Remove the setuptools dep as it doesn't add anything to the package and this way
  we wouldn't have to keep setuptools running on the python2 stack.

* Tue Sep 18 2018 Toshio Kuratomi <toshio@fedoraproject.org> - - 2.6-8
- Conditionalize the python2 and python3 builds.  This will allow the Python2
  build to be automatically omitted once Python2 is removed from Fedora and the
  spec file to be shared with EPEL builds.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.6-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.6-2
- Rebuild for Python 3.6

* Thu Nov 17 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.6-1
- Update to 2.6
- Modernize spec
- Run test suite

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5-2
- Add prettyprint of values
- Make the tracing decorator more transparent

* Fri Dec  5 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 2.5-1
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.4-1
- New upstream with some enhancements from severl people.
- Build with python3 support.

* Thu Apr 11 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 2.3-2
- New upstream release.
- README file from upstream's SCM
- Note patches we have for upstream

* Tue Mar 19 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.1-1
- Initial Fedora build


