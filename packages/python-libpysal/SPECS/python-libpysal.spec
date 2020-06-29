%global srcname libpysal

%if %{fedora} > 31
%bcond_without docs_rebuild
%else
%bcond_with docs_rebuild
%endif

Name:           python-%{srcname}
Version:        4.2.2
Release:        2%{?dist}
Summary:        Python Spatial Analysis Library core components

License:        BSD
URL:            https://pysal.org
# PyPI source doesn't include test data or docs.
Source0:        https://github.com/pysal/libpysal/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Test example datasets.
Source1:        https://s3.amazonaws.com/geoda/data/ncovr.zip
Source2:        https://github.com/sjsrey/newHaven/archive/master/newHaven.zip
Source3:        https://github.com/sjsrey/rio_grande_do_sul/archive/master/rio_grande_do_sul.zip
# Fix bs4 -> beautifulsoup4.
Patch0001:      https://github.com/pysal/libpysal/commit/3775ab64b3da870801400772c59ed612c6f52f93.patch
# Hard-code the list of datasets to not use the network.
Patch0002:      0001-Hard-code-list-of-example-datasets.patch
# https://github.com/pysal/libpysal/pull/240
Patch0003:      0002-Remove-calls-to-deprecated-removed-time.clock.patch
# https://github.com/pysal/libpysal/pull/242
Patch0004:      0003-Fix-syntax-errors.patch
# https://github.com/pysal/libpysal/pull/243
Patch0005:      0004-DOC-Fix-invalid-section-headings.patch
# https://github.com/pysal/libpysal/pull/244
Patch0006:      0005-Fix-and-simplify-filter_adjlist.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(beautifulsoup4)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(numpy) >= 1.3
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(scipy) >= 0.11
BuildRequires:  python3dist(setuptools)

BuildRequires:  python3dist(geomet)
BuildRequires:  python3dist(geopandas) >= 0.2
BuildRequires:  python3dist(matplotlib) >= 1.5.1
BuildRequires:  python3dist(networkx)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(nose-exclude)
BuildRequires:  python3dist(nose-progressive)
#BuildRequires:  python3dist(numba)
BuildRequires:  python3dist(rtree) >= 0.8
BuildRequires:  python3dist(sqlalchemy)

%description
Core components of PySAL - A library of spatial analysis functions. Modules
include computational geometry, input and output, spatial weights, and built-in
example datasets.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Core components of PySAL - A library of spatial analysis functions. Modules
include computational geometry, input and output, spatial weights, and built-in
example datasets.


%package -n     python-%{srcname}-doc
Summary:        Documentation for python-libpysal

%if %{with docs_rebuild}
BuildRequires:  pandoc
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(numpydoc)
BuildRequires:  python3dist(sphinx) >= 1.4.3
BuildRequires:  python3dist(sphinx-bootstrap-theme) >= 0.7
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinxcontrib-bibtex)
%endif

%description -n python-%{srcname}-doc
Documentation files for python-libpysal


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%if %{with docs_rebuild}
# Remove pre-built docs
rm -rf docs
%endif

mkdir pysal_data
unzip %SOURCE1 -d pysal_data/NCOVR
unzip %SOURCE2 -d pysal_data/newHaven
unzip %SOURCE3 -d pysal_data/Rio_Grande_do_Sul

%build
%py3_build

%if %{with docs_rebuild}
# generate html docs
PYTHONPATH=${PWD}/build/lib sphinx-build-3 docsrc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%else
mv docs html
%endif


%install
%py3_install


%check
export PYSALDATA=$PWD/pysal_data
%{__python3} setup.py test


%files -n python3-%{srcname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%files -n python-%{srcname}-doc
%doc html libpysal/examples
%license LICENSE.txt


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2.2-2
- Rebuilt for Python 3.9

* Sun Feb 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.2.2-1
- Update to latest version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Sep 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.1-1
- Update to latest version

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1.0-1
- Update to latest version

* Sat Mar 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.1-2
- Cleanup rpmlint warnings

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0.1-1
- Initial package.
