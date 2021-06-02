# the upstream name is io_lib, but it was deemed too generic, and
# staden-io_lib will be more recognizable for users
Name:           staden-io_lib
Version:        1.12.4
Release:        17%{?dist}
Summary:        General purpose library to handle gene sequencing machine trace files

License:        MIT
URL:            http://staden.sourceforge.net
Source0:        http://downloads.sourceforge.net/staden/io_lib-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  curl-devel zlib-devel

%description
The Staden I/O library provides a general purpose interface for reading and
writing trace files and other bioinformatics experiment files.  The programmer
simply calls, for example, the read_reading function to create a "Read" C
structure with the data loaded into memory.  It has been compiled and tested
on a variety of Unix systems, MacOS X and MS Windows.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# libread is too generic.  Make up something more specific.
# also fix config script name to include the staden- part
%setup -q -n io_lib-%{version}
mv io_lib-config.in staden-io_lib-config.in
sed -i 's/libread/libstaden-read/g' io_lib/Makefile.in progs/Makefile.in
sed -i 's/lread/lstaden-read/' staden-io_lib-config.in
sed -i 's/io_lib-config/staden-io_lib-config/g' configure Makefile.in


%build
%configure --disable-static
# make sure /lib64 /usr/lib64 are known to libtool to avoid rpath issues
sed -i 's+\(search_path_spec="\)+\1/lib64 /usr/lib64 +' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc README COPYRIGHT CHANGES docs/
%{_libdir}/*.so.*
%{_bindir}/append_sff
%{_bindir}/convert_trace
%{_bindir}/extract_fastq
%{_bindir}/extract_qual
%{_bindir}/extract_seq
%{_bindir}/get_comment
%{_bindir}/hash_extract
%{_bindir}/hash_list
%{_bindir}/hash_sff
%{_bindir}/hash_tar
%{_bindir}/index_tar
%{_bindir}/makeSCF
%{_bindir}/scf_dump
%{_bindir}/scf_info
%{_bindir}/scf_update
%{_bindir}/srf2fasta
%{_bindir}/srf2fastq
%{_bindir}/srf_dump_all
%{_bindir}/srf_extract_hash
%{_bindir}/srf_extract_linear
%{_bindir}/srf_filter
%{_bindir}/srf_index_hash
%{_bindir}/srf_info
%{_bindir}/srf_list
%{_bindir}/trace_dump
%{_bindir}/ztr_dump
%{_mandir}/man1/*

%files devel
%doc
%{_mandir}/man3/*
%{_mandir}/man4/*
%{_includedir}/io_lib/
%{_libdir}/*.so
%{_bindir}/staden-io_lib-config


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Christian Iseli <Christian.Iseli@licr.org> 1.12.4-1
- new upstream 1.12.4
- the library is now dynamic, so remove traces of static setup
- fix rpath issues
- re-phrase a bit the descrition to quieten rpmlint warnings

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun 12 2008 Christian Iseli <Christian.Iseli@licr.org> 1.11.2.1-2
- Avoid calling configure twice

* Wed Jun 11 2008 Christian Iseli <Christian.Iseli@licr.org> 1.11.2.1-1
- initial Fedora release

* Fri Jun  6 2008 Christian Iseli <Christian.Iseli@licr.org> 1.11.2.1-0
- new upstream 1.11.2.1
- change libread into libstaden-read
- change io_lib-config into staden-io_lib-config

* Tue Apr 29 2008 Christian Iseli <Christian.Iseli@licr.org> 1.11.0-0
- Initial RPM.
