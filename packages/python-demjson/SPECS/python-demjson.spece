%global srcname demjson

Name:           python-%{srcname}
Version:        2.2.4
Release:        19%{?dist}
Summary:        Python JSON module and lint checker
License:        LGPLv3+
URL:            http://deron.meranda.us/python/%{srcname}/
Source0:        http://deron.meranda.us/python/%{srcname}/dist/%{srcname}-%{version}.tar.gz
Patch0:         demjson_2.2.4_py39.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  %{_bindir}/2to3

%global base_description The demjson package is a comprehensive Python language library to read\
and write JSON; the popular language-independent data format standard.\
\
It includes a command tool, jsonlint, that allows you to easily check\
and validate any JSON document, and spot any potential data\
portability issues. It can also reformat and re-indent a JSON document\
to make it easier to read.

%description
%{base_description}


%package -n python3-%{srcname}
Summary:        Python JSON module and lint checker
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{base_description}


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install

# fix shebang lines
find %{buildroot}%{python3_sitelib} \
     -name '*.py' -exec \
     sed -i "1{/^#!/d}" {} \;


%check
pushd test
2to3 -w --no-diffs test_demjson.py
PYTHONPATH=%{buildroot}%{python3_sitelib} \
%{__python3} test_demjson.py
popd


%files -n python3-%{srcname}
%doc README.txt README.md
%doc docs
%license LICENSE.txt
%{python3_sitelib}/*
%{_bindir}/jsonlint


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-19
- Rebuilt for Python 3.9

* Sun Feb 23 2020 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-18
- Add patch for Python39 compatibility.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-16
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 27 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-15
- Remove Python2 subpackage (bz#1745780).

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-14
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-13
- %%{_bindir}/jsonlint uses Python3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jul 30 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-7
- Update BRs.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.4-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.4-1
- Update to 2.2.4.
- Follow updated Python packaging guidelines.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.3-1
- Update to 2.2.3.
- Apply updated Python packaging guidelines.
- Mark LICENSE.txt with %%license.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 25 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.2-1
- Update to 2.2.2.
- Provide python3 subpackage.
- Modernize spec file.
- Update %%description.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Apr  4 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.6-1
- Update to 1.6.
- Injecting setuptools is only needed for EPEL5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.5-1
- Update to 1.5.
- Remove patch no longer needed.

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.4-1
- Update to 1.4. Upstream changed license to LGPLv3+.
- Apply a one-liner patch provided upstream.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3-3
- Rebuild for Python 2.6

* Mon Mar 31 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.3-2
- Cleanup BuildRequires.
- Don't pack INSTALL.txt.

* Thu Mar 27 2008 Thomas Moschny <thomas.moschny@gmx.de> - 1.3-1
- New package.
