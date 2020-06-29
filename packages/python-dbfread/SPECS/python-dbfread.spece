%global pypi_name dbfread
%global project_owner olemb
%global github_name dbfread
%global commit 300b2d7d907388cc3578d3fa4472e0419ccd34b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global desc DBF is a file format used by databases such dBase, Visual FoxPro, and \
FoxBase+. This library reads DBF files and returns the data as native Python \
data types for further processing. It is primarily intended for batch jobs and \
one-off scripts.\
\
Full documentation at https://dbfread.readthedocs.io/\
\
See docs/changes.rst for a full list of changes in each version.


Name:           python-%{pypi_name}
Version:        2.0.7
Release:        15.git%{shortcommit}%{?dist}
Summary:        Read DBF Files with Python

License:        MIT
URL:            https://pypi.python.org/pypi/dbfread
Source0:        https://github.com/%{project_owner}/%{github_name}/archive/%{commit}/%{github_name}-%{commit}.tar.gz
# Fix tests with pytest4
Patch0:         https://patch-diff.githubusercontent.com/raw/olemb/dbfread/pull/33.patch
BuildArch:      noarch

%description
%{desc}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}


%package -n    python-%{pypi_name}-doc
Summary:       %{summary}
BuildRequires:  python3dist(sphinx)
BuildArch:     noarch

%description -n python-%{pypi_name}-doc
%{desc}

Documentation package.


%prep
%setup -qn %{github_name}-%{commit}
# Remove shebang in examples
sed -i '1{\@^#!/usr/bin/env python@d}' examples/{*.py,**/*.py,dbf2sqlite}
# Make sure examples are not executable
chmod -x examples/{*.py,**/*.py,dbf2sqlite}
%patch0 -p1


%build
%py3_build

# Build documentation
pushd docs
    make html SPHINXBUILD=sphinx-build-%{python3_version}
    rm -f _build/html/.buildinfo
popd


%install
%py3_install


%check
# The script will launch pytest for Python 2 and 3.
pytest-%{python3_version}


%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{pypi_name}/


%files -n python-%{pypi_name}-doc
%license LICENSE
%doc README.rst docs/_build/ examples


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.7-15.git300b2d7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-14.git300b2d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.7-13.git300b2d7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.7-12.git300b2d7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-11.git300b2d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Julien Enselme <jujens@jujens.eu> - 2.0.7-10.git300b2d7
- Fix tests with pytest4

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-9.git300b2d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Julien Enselme <jujens@jujens.eu> - 2.0.7-8
- Remove Python 2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-7.git300b2d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.7-6.git300b2d7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-5.git300b2d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.7-4.git300b2d7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Julien Enselme <jujens@jujens.eu> - 2.0.7-3.git300b2d7
- Fix shebang in examples

* Mon Mar 13 2017 Julien Enselme <jujens@jujens.eu> - 2.0.7-2.git300b2d7
- Add dependency to sphinx to build the documentation

* Sun Mar 12 2017 Julien Enselme <jujens@jujens.eu> - 2.0.7-1.git300b2d7
- Inital package
