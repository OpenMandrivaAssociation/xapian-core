%define oname xapian
%define major 15
%define libname %mklibname %{oname} %{major}
%define develname %mklibname %{oname} -d

Summary:	Search engine library
Name:           xapian-core
Version:	1.0.18
Release:        %mkrel 1
License:	GPLv2+
Group:		Databases
URL:		http://www.xapian.org/
Source0:	http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	zlib-devel
BuildRequires:	valgrind
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	xapian < 1.0.7
Provides:	xapian
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Xapian is an Open Source Search Engine Library, released under the 
GPL. It's written in C++, with bindings to allow use from Perl, 
Python, PHP, Java, Tcl, C#, and Ruby (so far!)

Xapian is a highly adaptable toolkit which allows developers to easily
add advanced indexing and search facilities to their own applications. 
It supports the Probabilistic Information Retrieval model and also 
supports a rich set of boolean query operators.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%package  -n %{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{oname}-devel = %{version}-%{release}
Provides:	lib%{oname}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
%ifarch x86_64
chrpath -d %{buildroot}%{_bindir}/copydatabase
chrpath -d %{buildroot}%{_bindir}/delve
chrpath -d %{buildroot}%{_bindir}/quartzcheck
chrpath -d %{buildroot}%{_bindir}/quartzcompact
chrpath -d %{buildroot}%{_bindir}/quartzdump
chrpath -d %{buildroot}%{_bindir}/quest
chrpath -d %{buildroot}%{_bindir}/simpleexpand
chrpath -d %{buildroot}%{_bindir}/simpleindex
chrpath -d %{buildroot}%{_bindir}/simplesearch
chrpath -d %{buildroot}%{_bindir}/xapian-compact
chrpath -d %{buildroot}%{_bindir}/xapian-progsrv
chrpath -d %{buildroot}%{_bindir}/xapian-tcpsrv
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_bindir}/copydatabase
%{_bindir}/delve
%{_bindir}/quartzcheck
%{_bindir}/quartzcompact
%{_bindir}/quartzdump
%{_bindir}/quest
%{_bindir}/simpleexpand
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/xapian-compact
%{_bindir}/xapian-check
%{_bindir}/xapian-progsrv
%{_bindir}/xapian-tcpsrv
%{_bindir}/xapian-inspect
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxapian.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/xapian-config
%doc %{_docdir}/%{name}/
%dir %{_includedir}/xapian
%{_includedir}/xapian/*.h
%{_includedir}/*.h
%{_datadir}/aclocal/xapian.m4
%{_libdir}/libxapian.a
%{_libdir}/libxapian.la
%{_libdir}/libxapian.so
