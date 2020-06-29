%global srcname latexcodec

Name:           python-%{srcname}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Lexer and codec to work with LaTeX code in Python

License:        MIT
URL:            https://github.com/mcmtroffaes/latexcodec/
Source0:        %pypi_source
BuildArch:      noarch

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-docs
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%description
This package contains a lexer and codec to work with LaTeX code in Python.

%package -n python3-%{srcname}
Summary:        Lexer and codec to work with LaTeX code in Python
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This package contains a lexer and codec to work with LaTeX code in Python.

%package doc
Summary:        Documentation for %{name}
Provides:       bundled(jquery)
Provides:       bundled(js-underscore)

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{srcname}-%{version}

# Update the sphinx theme name
sed -i 's/default/classic/' doc/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('http://docs\.python\.org/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" doc/conf.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel
PYTHONPATH=$PWD make -C doc html
rm -f doc/_build/html/.buildinfo
rst2html --no-datestamp LICENSE.rst LICENSE.html

%install
%pyproject_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest

%files -n python3-%{srcname}
%license LICENSE.html
%{python3_sitelib}/%{srcname}*

%files doc
%license LICENSE.html
%doc doc/_build/html/*

%changelog
* Tue Jun 23 2020 Jerry James <loganjerry@gmail.com> - 2.0.1-1
- Version 2.0.1

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Jerry James <loganjerry@gmail.com> - 2.0.0-1
- Version 2.0.0 (bz 1789613, 1791202)
- Add -doc subpackage
- Use pytest instead of nose
- Use local objects.inv to create documentation links

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May  3 2019 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- New upstream version
- Drop upstreamed -hyphen patch

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 1.0.5-6
- Drop python2 subpackage (bz 1647376)
- Add -hyphen patch

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2
- Rebuild for Python 3.6

* Thu Sep 22 2016 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- New upstream version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 26 2016 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- New upstream version

* Fri Mar  4 2016 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- New upstream version

* Tue Feb  2 2016 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Initial RPM
