%{?python_enable_dependency_generator}
%global srcname     nixio

Name:       python-%{srcname}
Version:    1.4.9
Release:    10%{?dist}
Summary:    Python bindings for NIX

License:    BSD
URL:        https://github.com/G-node/nixpy
Source0:    https://github.com/G-node/nixpy/archive/%{version}/%{name}-%{version}.tar.gz


BuildArch:      noarch
# No need for nix, they're uncoupling it from the C++
# https://github.com/G-Node/nixpy/pull/276

%description
The NIX project started as an initiative within the Electrophysiology Task
Force a part of the INCF Data sharing Program. The NIX data model allows to
store fully annotated scientific data-set, i.e. the data together with its
metadata within the same container. Our aim is to achieve standardization by
providing a common/generic data structure for a multitude of data types. See
the wiki for more information

The current implementations store the actual data using the HDF5 file format as
a storage backend.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  %{py3_dist h5py}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-runner}
BuildRequires:  %{py3_dist setuptools}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
The NIX project started as an initiative within the Electrophysiology Task
Force a part of the INCF Data sharing Program. The NIX data model allows to
store fully annotated scientific data-set, i.e. the data together with its
metadata within the same container. Our aim is to achieve standardization by
providing a common/generic data structure for a multitude of data types. See
the wiki for more information

The current implementations store the actual data using the HDF5 file format as
a storage backend.

%package doc
Summary:        %{summary}
BuildRequires:  python3-sphinx

%description doc
Documentation files for %{name}.

%prep
%autosetup -n nixpy-%{version}
rm -fr *egg-info

%build
%py3_build

PYTHONPATH=. sphinx-build-3 docs/source html
# Remove unneeded files
rm -fr html/.{buildinfo,doctrees}

# Remove shebang from documentation examples
for f in html/_downloads/*/*.py; do
    sed '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info
%{python3_sitelib}/%{srcname}/

%files doc
%doc README.rst html
%license LICENSE

%changelog
* Thu Jun 25 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.9-10
- Explicitly BR setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.9-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.9-4
- Fix build: rhbz 1706159

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.9-2
- Enable python dependency generator

* Sat Jan 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.9-1
- Update to 1.4.9

* Thu Oct 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.6-2
- Subpackage python2-nixio has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jul 18 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.6-1
- Update to 1.4.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.5-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.5-1
- Update to latest upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.3-1
- Use newer release and GitHub sources
- Run tests
- Define summary macro
- Add doc sub package

* Fri Jan 12 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.2-1
- Initial build
- use pydist macro
